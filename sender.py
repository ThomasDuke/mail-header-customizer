import wx
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import dns.resolver

class EmailApp(wx.Frame):
    def __init__(self, parent, title):
        super(EmailApp, self).__init__(parent, title=title, size=(700, 500))

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.subject_label = wx.StaticText(self.panel, label="Subject:")
        self.subject_input = wx.TextCtrl(self.panel)
        
        # Bouton pour vérifier l'enregistrement DMARC
        self.check_dmarc_button = wx.Button(self.panel, label="DMARC Check")
        self.check_dmarc_button.Bind(wx.EVT_BUTTON, self.on_check_dmarc)

        self.from_label = wx.StaticText(self.panel, label="From:")
        self.from_input = wx.TextCtrl(self.panel)

        self.to_label = wx.StaticText(self.panel, label="To:")
        self.to_input = wx.TextCtrl(self.panel)

        # Contrôle de choix pour sélectionner le mode texte ou le mode HTML
        self.mode_choice = wx.Choice(self.panel, choices=["Text", "HTML"])
        self.mode_choice.Bind(wx.EVT_CHOICE, self.on_mode_select)

        # Zone de saisie de texte plus grande pour le message
        self.message_input = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_RICH2)

        # Case à cocher pour activer l'ajout d'en-têtes personnalisés
        self.add_headers_checkbox = wx.CheckBox(self.panel, label="Add Headers")
        self.add_headers_checkbox.Bind(wx.EVT_CHECKBOX, self.on_add_headers)

        # Champ de saisie pour les en-têtes personnalisés (initialement caché)
        self.headers_input = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_RICH2)
        self.headers_input.Hide()

        self.send_button = wx.Button(self.panel, label="Send")
        self.send_button.Bind(wx.EVT_BUTTON, self.on_send)

        vbox.Add(self.from_label, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.from_input, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.check_dmarc_button, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.to_label, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.to_input, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.subject_label, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.subject_input, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.mode_choice, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.message_input, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.add_headers_checkbox, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.headers_input, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.send_button, flag=wx.EXPAND|wx.ALL, border=5)

        self.panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def on_send(self, event):
        smtp_server = "smtp-relay.brevo.com"
        port = 587
        sender_email = ""
        password = ""
        receiver_email = self.to_input.GetValue()

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject_input.GetValue()
        message["From"] = self.from_input.GetValue()
        message["To"] = receiver_email


        if self.add_headers_checkbox.GetValue():
            custom_headers = self.headers_input.GetValue()
            for header in custom_headers.split('\n'):
                if ':' in header:
                    header_key, header_value = header.split(':', 1)
                    message[header_key.strip()] = header_value.strip()


        # En fonction du mode sélectionné, définir la partie texte ou la partie HTML
        if self.mode_choice.GetSelection() == 0:  # Mode Text
            text = self.message_input.GetValue()
            part1 = MIMEText(text, "plain")
            message.attach(part1)
        else:  # Mode HTML
            html = self.message_input.GetValue()
            part2 = MIMEText(html, "html")
            message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            success_dialog = wx.MessageDialog(self.panel, "Email sent successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
            success_dialog.ShowModal()

    def on_mode_select(self, event):
        selected_mode = self.mode_choice.GetSelection()
        if selected_mode == 0:  # Mode Text
            self.message_input.SetWindowStyle(wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        else:  # Mode HTML
            self.message_input.SetWindowStyle(wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_RICH2)
        self.panel.Layout()

    def on_add_headers(self, event):
        if self.add_headers_checkbox.GetValue():
            self.headers_input.Show()
        else:
            self.headers_input.Hide()
        self.panel.Layout()

    def on_check_dmarc(self, event):
        domain = re.search("@[\w.-]+", self.from_input.GetValue())
        if domain:
            domain = domain.group(0)[1:]  # Extraction du domaine
            dmarc_record = self.fetch_dmarc_record(domain)
            if dmarc_record:
                # Si un enregistrement DMARC est trouvé, l'afficher
                if "p=none" in dmarc_record:
                    dmarc_record += "\nThe domain has a permissive policy."
                    result_dialog = wx.MessageDialog(self.panel, dmarc_record, "DMARC Record", wx.OK | wx.ICON_INFORMATION)
                    result_dialog.ShowModal()
                else:
                    dmarc_record += "\nThe domain has a restrictive policy."
                    result_dialog = wx.MessageDialog(self.panel, dmarc_record, "DMARC Record", wx.OK | wx.ICON_INFORMATION)
                    result_dialog.ShowModal()
            else:
                # Si aucun enregistrement DMARC n'est trouvé, afficher un message approprié
                result_dialog = wx.MessageDialog(self.panel, "No DMARC record found for this domain.", "DMARC record", wx.OK | wx.ICON_INFORMATION)
                result_dialog.ShowModal()
        else:
            wx.MessageBox("Please enter a valid e-mail address in the 'From' header.", "Error", wx.OK | wx.ICON_ERROR)

    def fetch_dmarc_record(self, domain):
        try:
            # Récupération de l'enregistrement DMARC à l'aide de dnspython
            answers = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
            for rdata in answers:
                return rdata.to_text()
        except dns.resolver.NoAnswer:
            return None
        except dns.resolver.NXDOMAIN:
            return None
        except Exception as e:
            print(f"An error has occured during the DMARC record retrieval : {e}")
            return None

app = wx.App()
EmailApp(None, title="Email Sender")
app.MainLoop()
