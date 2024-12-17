import tkinter as tk
from PIL import Image, ImageTk
import pygame
class AdventureGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ο Χριστουγεννιάτικος Φάρος")
        self.window.geometry("1080x1080")
        self.window.configure(bg="black")
        pygame.mixer.init()
        self.story_text = tk.StringVar()
        self.story_text.set("Παραμονή Χριστουγέννων του έτους 1900.")
        self.label = tk.Label(self.window, textvariable=self.story_text, wraplength=700, font=("Arial", 14),
                              justify="center", bg="black", fg="white")
        self.label.pack(pady=20)
        self.image_label = tk.Label(self.window, bg="black")
        self.image_label.pack(pady=20)
        self.button1 = tk.Button(self.window, text="", width=30, bg="black", fg="white", highlightbackground="black")
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self.window, text="", width=30, bg="black", fg="white", highlightbackground="black")
        self.button2.pack(pady=5)
        self.button3 = tk.Button(self.window, text="", width=30, bg="black", fg="white", highlightbackground="black")
        self.button3.pack(pady=5)
        self.current_state = "intro"
        self.update_state("intro")
        self.window.mainloop()
    def play_sound(self, sound_file):
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print(f"Error loading sound: {e}")
    def stop_sound(self):
        pygame.mixer.music.stop()
    def update_image(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((420, 420), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")
    def update_state(self, state):
        self.current_state = state
        self.stop_sound()
        if state == "intro":
            self.story_text.set(
                "Παραμονή Χριστουγέννων του έτους 1950. Οι Νήσοι Φλάναν, "
                "ένα απομονωμένο σύμπλεγμα στα παγωμένα νερά του Ατλαντικού, "
                "σκεπάζονται από ένα πέπλο ομίχλης και θρύλων. Εκεί, στην πιο απόμερη γωνιά τους, "
                "ο φάρος του Έιλιαν Μορ στέκεται αγέρωχος, η μοναδική μαρτυρία ανθρώπινης παρουσίας "
                "στο άγριο τοπίο. Το φως του τρεμοπαίζει αδύναμα, σαν να προσπαθεί να ακουστεί "
                "μέσα στο χάος της καταιγίδας. "
            )
            self.update_image("intro.jpg")
            self.play_sound("intro.wav")
            self.button1.config(text="Επόμενη σελίδα", command=lambda: self.update_state("intro2"))
            self.button2.config(text="", command=lambda: None)
            self.button3.config(text="", command=lambda: None)
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "intro2":
            self.story_text.set(
                "Ο άνεμος τραγουδά έναν σκοτεινό ύμνο, κουβαλώντας ιστορίες "
                "για τους τρεις φύλακες του φάρου που εξαφανίστηκαν πριν έναν χρόνο, "
                "αφήνοντας πίσω τους μόνο στολισμένα δωμάτια, ένα ημερολόγιο γεμάτο παράξενες αναφορές, "
                "και τη διαρκή αναλαμπή ενός φωτός που δεν έσβησε ποτέ. Οι χωρικοί μιλούν για ένα πνεύμα "
                "που επιστρέφει κάθε Χριστούγεννα, ζητώντας απαντήσεις ή δικαίωση. "
            )
            self.update_image("old.jpg")
            self.play_sound("keepers.wav")
            self.button1.config(text="Επόμενη σελίδα", command=lambda: self.update_state("intro3"))
            self.button2.config(text="", command=lambda: None)
            self.button3.config(text="", command=lambda: None)
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "intro3":
            self.story_text.set(
                "Μια φουρτούνα σε παρέσυρε και σε πέταξε στις ακτές του νησιού. "
                "Τώρα, ο φάρος είναι η μόνη σου ελπίδα για καταφύγιο. "
                "Τα φώτα του, στολισμένα με γιρλάντες και ξεθωριασμένα λαμπιόνια, "
                "στέλνουν ένα αινιγματικό μήνυμα μέσα από την ομίχλη. "
                "Κάθε βήμα που κάνεις προς το κτίσμα συνοδεύεται από έναν παράξενο ήχο, "
                "σαν κουδουνίσματα – οικεία, αλλά και ανατριχιαστικά. \n "
                "Οι Νήσοι Φλάναν έχουν τους δικούς τους κανόνες. "
                "Κάτι σε παρακολουθεί. Ο φάρος σε καλεί. Θα απαντήσεις; "
            )
            self.update_image("intro3.jpg")
            self.play_sound("wind-sea.mp3")
            self.button1.config(text="Επόμενη σελίδα", command=lambda: self.update_state("start"))
            self.button2.config(text="", command=lambda: None)
            self.button3.config(text="", command=lambda: None)
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "start":
            self.story_text.set(
                "Ο άνεμος φυσάει παγωμένος, και η παραλία μοιάζει ατελείωτη. "
                "Το χιόνι τρίζει κάτω από τα πόδια σου, ενώ μπροστά σου δεσπόζει ο φάρος, "
                "μια μοναχική φιγούρα στη μέση του χειμερινού τοπίου.Το μικρό παρεκκλήσι στα δεξιά "
                "φαίνεται σχεδόν χαμένο μέσα στην ομίχλη. Αλλά τα βήματα που έχουν σχηματιστεί στο χιόνι "
                "και οδηγούν στο δάσος φαίνονται να έχουν δημιουργηθεί πρόσφατα."
            )
            self.update_image("snow.jpg")
            self.play_sound("winds.wav")
            self.button1.config(text="Προχωράς προς τον φάρο", command=lambda: self.update_state("lighthouse"))
            self.button2.config(text="Εξερευνάς το παρεκκλήσι", command=lambda: self.update_state("chapel"))
            self.button3.config(text="Ακολουθείς τα βήματα στο δάσος", command=lambda: self.update_state("forest"))
            self.button2.pack()
            self.button3.pack()
        elif state == "lighthouse":
            self.story_text.set(
                "Φτάνεις στον φάρο και μπαίνεις μέσα. Το κρύο είναι παγωμένο και ακούγεται ένα "
                "βαρύ βουητό. Υπάρχουν παντού σκορπισμένα αντικέιμενα, μία σκάλα που φτάνει μέχρι την κορυφή "
                "και μία πόρτα που οδηγεί στο υπόγειο. Τί θα κάνεις;"
            )
            self.update_image("lighhouse-interior.jpg")
            self.play_sound("ambient-hum.wav")
            self.button1.config(text="Ανεβαίνεις την σκάλα", command=lambda: self.update_state("lighthouse_top"))
            self.button2.config(text="Ανοίγεις την πόρτα", command=lambda: self.update_state("basement"))
            self.button3.config(text="Ψάχνεις στον χώρο", command=lambda: self.update_state("inside"))
            self.button2.pack()
            self.button3.pack()
        elif state == "chapel":
            self.story_text.set(
                "Το παρεκκλήσι είναι παλιό και φθαρμένο. "
                "Οι τοίχοι του είναι σκεπασμένοι με μούχλα, "
                "και τα παράθυρα του φαίνονται να έχουν παραμείνει κλειστά"
                "αρκετά χρόνια. "
                "Μια παγωμένη αύρα σε τυλίγει καθώς πλησιάζεις "
                "και οι τοίχοι έχουν περίεργες χαρακιές σαν από νύχια."
            )
            self.update_image("chappel.jpg")
            self.play_sound("chappel.wav")
            self.button1.config(text="Μπαίνεις μέσα", command=lambda: self.update_state("chapel_inside"))
            self.button3.config(text="Επιστρέφεις στην ακτή", command=lambda: self.update_state("start"))
            self.button2.pack_forget()
            self.button3.pack()
        elif state == "chapel2":
            self.story_text.set(
                "Το παρεκκλήσι είναι παλιό και φθαρμένο. "
                "Οι τοίχοι του είναι σκεπασμένοι με μούχλα, "
                "και τα παράθυρα του φαίνονται να έχουν παραμείνει κλειστά"
                "αρκετά χρόνια. "
                "Μια παγωμένη αύρα σε τυλίγει καθώς πλησιάζεις "
                "και οι τοίχοι έχουν περίεργες χαρακιές σαν από νύχια."
            )
            self.update_image("chappel.jpg")
            self.play_sound("chappel.wav")
            self.button1.config(text="Μπαίνεις μέσα", command=lambda: self.update_state("chapel_inside2"))
            self.button3.config(text="Επιστρέφεις στην ακτή", command=lambda: self.update_state("start"))
            self.button2.pack_forget()
            self.button3.pack()
        elif state == "chapel_inside":
            self.story_text.set(
                "Μπαίνοντας μέσα, τα πάντα είναι σκοτεινά."
                "Ένα άσχημο προαίσθημα σε κατακλύζει."
                "Ακούς έντονους θορύβους απο το βάθος. Πριν προλάβεις να αντιληφθείς "
                "τι γίνεται ένα διαβολικό πλάσμα έρχεται και σε σκοτώνει."
            )
            self.update_image("monster.jpg")
            self.play_sound("beast.wav")
            self.button1.config(text="Τέλος παιχνιδιού", command=lambda: self.update_state("end"))
            self.button2.config(text="Προσπάθησε ξανά", command=lambda: self.update_state("start"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "chapel_inside2":
            self.story_text.set(
                "Μπαίνοντας μέσα, ένα διαβολικό πλάσμα έρχεται και τότε χωρίς να ξέρεις γιατί"
                "φωνάζεις με όλη σου την δύναμη IMPERIO."
                "Μία τεράστια λάμψη ξεχύνεται σε όλο τον χώρο."
                "κι εσύ κατάφερες να νικήσεις το τέρας."
                "Τρέχεις προς την έξοδο."
            )
            self.update_image("light.jpg")
            self.play_sound("beast.wav")
            self.button1.config(text="Βγες έξω", command=lambda: self.update_state("start3"))
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "forest":
            self.story_text.set(
                "Το δάσος είναι σκοτεινό και τρομακτικό. Περπατάς ανάμεσα στα δέντρα με σπασμένα "
                "χριστουγεννιάτικα στολίδια. Βλέπεις μια καλύβα. Θα μπεις;"
            )
            self.update_image("woods2.jpg")
            self.play_sound("woods.wav")
            self.button1.config(text="Μπαίνεις στην καλύβα", command=lambda: self.update_state("cabin"))
            self.button2.config(text="Συνεχίζεις στο μονοπάτι", command=lambda: self.update_state("car"))
            self.button3.config(text="Επιστρέφεις στην παραλία", command=lambda: self.update_state("start"))
            self.button2.pack()
            self.button3.pack()
        elif state == "forest2":
            self.story_text.set(
                "Το δάσος είναι σκοτεινό και τρομακτικό. Περπατάς ανάμεσα στα δέντρα με σπασμένα "
                "χριστουγεννιάτικα στολίδια. Βλέπεις μια καλύβα. Θα μπεις;"
            )
            self.update_image("woods2.jpg")
            self.play_sound("woods.wav")
            self.button1.config(text="Μπαίνεις στην καλύβα", command=lambda: self.update_state("cabin2"))
            self.button2.config(text="Συνεχίζεις στο μονοπάτι", command=lambda: self.update_state("forest_path"))
            self.button3.config(text="Επιστρέφεις στην παραλία", command=lambda: self.update_state("start"))
            self.button2.pack()
            self.button3.pack()
        elif state == "cabin":
            self.story_text.set(
                "Μπαίνοντας στην καλύβα, καταλαβαίνεις οτι δεν είσαι μόνος."
                "Ένας άντρας με καλυμμένο το πρόσωπο του, έρχεται καταπάνω σου με ένα μαχαίρι."
                "Δυστυχώς δεν έχεις κάποιο όπλο πάνω σου και σε σκοτώνει."
            )
            self.update_image("man.jpg")
            self.play_sound("man.mp3")
            self.button1.config(text="Τέλος παιχνιδιού", command=lambda: self.update_state("end"))
            self.button2.config(text="Προσπάθησε ξανά", command=lambda: self.update_state("start"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "cabin2":
            self.story_text.set(
                "Μπαίνοντας στην καλύβα, καταλαβαίνεις οτι δεν είσαι μόνος."
                "Ένας άντρας με καλυμμένο το πρόσωπο του, έρχεται καταπάνω σου με ένα μαχαίρι."
                "Ευτυχώς έχεις το όπλο και τραβάς κατευθείαν την σκανδάλη.."
                "Τώρα μπορείς ελεύθερα να εξερευνήσεις τον χώρο."
            )
            self.update_image("gunfire.jpg")
            self.play_sound("gunfire.mp3")
            self.button1.config(text="Εξερευνάς τον χώρο", command=lambda: self.update_state("key"))
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "key":
            self.story_text.set(
                "Ψάχνοντας λίγο καλύτερα στον χώρο, βρίσκεις πεσμένο ένα κλειδί αυτοκινήτου."
                "Το παίρνεις και βγαίνεις έξω."
            )
            self.update_image("carkey.jpg")
            self.play_sound("hint.wav")
            self.button1.config(text="Βγαίνεις έξω", command=lambda: self.update_state("car2"))
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "car":
            self.story_text.set(
                "Προχωρώντας προς το μονοπάτι, βλέπεις ένα αυτοκίνητο. "
                "Δεν καθυστερείς καθόλου και τρέχεις γρήγορα να μπεις μέσα."
                "Η πόρτα είναι κλειδωμένη! Πρέπει να βρεις το κλειδί."
            )
            self.update_image("keynot.jpg")
            self.play_sound("woods.wav")
            self.button1.config(text="Πήγαινε πίσω", command=lambda: self.update_state("forest"))
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "car2":
            self.story_text.set(
                "Προχωρώντας προς το μονοπάτι, βλέπεις ένα αυτοκίνητο. "
                "Δεν καθυστερείς καθόλου και τρέχεις γρήγορα να μπεις μέσα."
                "Τα κατάφερες! Λίγα χιλιόμετρα παρακάτω, υπάρχει ένα χωριό"
                "που μπορείς να βρεις ασφαλές καταφύγιο και να επικοινωνήσεις "
                "με τους δικούς σου ανθρώπους."
            )
            self.update_image("carwin.jpg")
            self.play_sound("carwin.wav")
            self.button1.config(text="Τέλος", command=lambda: self.update_state("Victory"))
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "Victory":
            self.story_text.set(
                "You won!!!"
            )
            self.update_image("win.jpg")
            self.play_sound("victory.mp3")
            self.window.after(4000, self.window.destroy)
            self.button1.pack_forget()
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "inside":
            self.story_text.set(
                "Ψάχνοντας καλύτερα τον χώρο βλέπεις ένα σκουριασμένο κλειδί. Ίσως ανοίγει κάποια πόρτα..."
            )
            self.update_image("key.jpg")
            self.play_sound("key.wav")
            self.button1.config(text="Προχωράς προς το υπόγειο", command=lambda: self.update_state("basement2"))
            self.button2.config(text="Ανεβαίνεις την σκάλα", command=lambda: self.update_state("lighthouse_top"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "lighthouse2":
            self.story_text.set(
                "Φτάνεις στον φάρο και μπαίνεις μέσα. Το κρύο είναι παγωμένο και ακούγεται ένα "
                "βαρύ βουητό. Υπάρχουν παντού σκορπισμένα αντικέιμενα, μία σκάλα που φτάνει μέχρι την κορυφή "
                "και μία πόρτα που οδηγεί στο υπόγειο. Τί θα κάνεις;"
            )
            self.update_image("lighhouse-interior.jpg")
            self.play_sound("ambient-hum.wav")
            self.button1.config(text="Ανεβαίνεις την σκάλα", command=lambda: self.update_state("lighthouse_top"))
            self.button2.config(text="Ανοίγεις την πόρτα", command=lambda: self.update_state("basement2"))
            self.button2.pack()  # Show button2
            self.button3.pack_forget()  # Show button3
        elif state == "basement":
            self.story_text.set(
                "Προσπαθείς να ανοίξεις την πόρτα, αλλά είναι κλειδωμένη. "
                "Ίσως τελικά υπάρχει κάτι στον χώρο που δεν παρατήρησες καλά..."
            )
            self.update_image("basement.jpg")
            self.play_sound("locked.wav")
            self.button1.config(text="Γύρνα πίσω", command=lambda: self.update_state("lighthouse"))
            self.button2.pack_forget()  # Show button2
            self.button3.pack_forget()  # Show button3
        elif state == "basement2":
            self.story_text.set(
                "Προσπαθείς να ανοίξεις την πόρτα με το κλειδί. "
                "Μετά απο λίγα δευτερόλεπτα ανοίγει. Μπαίνεις μέσα ή μήπως φοβάσαι;"
            )
            self.update_image("door2.jpg")
            self.play_sound("open.wav")
            self.button1.config(text="Γύρνα πίσω", command=lambda: self.update_state("lighthouse2"))
            self.button2.config(text="Μπαίνεις μέσα", command=lambda: self.update_state("basement-inside"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "basement-inside":
            self.story_text.set(
                "Το υπόγειο είναι τόσο σκοτεινό που δεν μπορείς να δεις καθόλου καθαρά. "
                "Μπορείς να ανάψεις τον διακόπτη που βρίσκεται στα δεξιά σου "
                "ή να συνεχίσεις να περπατάς στο σκοτάδι."
            )
            self.update_image("dark-room.jpg")
            self.play_sound("silence.wav")
            self.button1.config(text="Περπατάς στο σκοτάδι", command=lambda: self.update_state("death2"))
            self.button2.config(text="Ανάβεις το φως", command=lambda: self.update_state("basement-light"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "basement-light":
            self.story_text.set(
                "Το φως αποκαλύπτει διάφορα σημεία στον χώρο, "
                "αλλά αυτό που σου κεντρίζει πιο πολύ την προσοχή "
                "είναι ένα βιβλίο και ένα κουτί."
            )
            self.update_image("books-boxes.jpg")
            self.play_sound("silence.wav")
            self.button1.config(text="Ανοίγεις το κουτί", command=lambda: self.update_state("box"))
            self.button2.config(text="Διαβάζεις το βιβλίο", command=lambda: self.update_state("book"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "book":
            self.story_text.set(
                "Ανοίγωντας το βιβλίο, παρατηρείς ότι περιέχει περίεργα σύμβολα "
                "και λέξεις που δεν ξέρεις τι σημαίνουν. Μόνο μία φαίνεται να πέφτει στο μάτι σου. "
                "IMPERIO. "
                "Τί να σημαίνει άραγε; "
                "Αφού τελειώνεις το βιβλίο, καταλαβαίνεις ότι το υπόγειο δεν έχει κάτι άλλο "
                "που θα σε βοηθήσει να φύγεις απο το νησί."
            )
            self.update_image("spell.jpg")
            self.play_sound("silence.wav")
            self.button1.config(text="Επιστρέφεις πίσω στην ακτή", command=lambda: self.update_state("start2"))
            self.button2.pack_forget()
            self.button3.pack_forget()
        elif state == "box":
            self.story_text.set(
                "Ανοίγωντας το κουτί, παρατηρείς ότι περιέχει μέσα ένα τυλιγμένο αντικείμενο "
                "Ξετυλίγοντάς το, διαπιστώνεις ότι είναι ένα όπλο γεμισμένο με έξι σφαίρες. "
                "Αφήνοντας το κάτω, καταλαβαίνεις ότι το υπόγειο δεν έχει κάτι άλλο "
                "που θα σε βοηθήσει να φύγεις απο το νησί."
            )
            self.update_image("gun2.jpg")
            self.play_sound("silence.wav")
            self.button1.config(text="Επιστρέφεις στην ακτή, με το όπλο", command=lambda: self.update_state("start4"))
            self.button2.config(text="Επιστρέφεις στην ακτή, χωρίς το όπλο", command=lambda: self.update_state("start"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "start2":
            self.story_text.set(
                "Το μικρό παρεκκλήσι στα δεξιά "
                "φαίνεται σχεδόν χαμένο μέσα στην ομίχλη. Αλλά τα βήματα που έχουν σχηματιστεί στο χιόνι "
                "και οδηγούν στο δάσος φαίνονται να έχουν δημιουργηθεί πρόσφατα."
            )
            self.update_image("snow.jpg")
            self.play_sound("winds.wav")
            self.button1.config(text="Εξερευνάς το παρεκκλήσι", command=lambda: self.update_state("chapel2"))
            self.button2.config(text="Ακολουθείς τα βήματα στο δάσος", command=lambda: self.update_state("forest"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "start3":
            self.story_text.set(
                "Η μόνη κατεύθυνση που σου έχει μείνει είναι "
                "να ακολουθήσεις τα βήματα προς το δάσος, ή μήπως ξέχασες κάτι..."
            )
            self.update_image("snow.jpg")
            self.play_sound("winds.wav")
            self.button1.config(text="Πας προς το δάσος", command=lambda: self.update_state("forest"))
            self.button1.config(text="Πάρε όπλο", command=lambda: self.update_state("cabin2"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "start4":
            self.story_text.set(
                "Το μικρό παρεκκλήσι στα δεξιά "
                "φαίνεται σχεδόν χαμένο μέσα στην ομίχλη. Αλλά τα βήματα που έχουν σχηματιστεί στο χιόνι "
                "και οδηγούν στο δάσος φαίνονται να έχουν δημιουργηθεί πρόσφατα."
            )
            self.update_image("snow.jpg")
            self.play_sound("winds.wav")
            self.button1.config(text="Εξερευνάς το παρεκκλήσι", command=lambda: self.update_state("chapel"))
            self.button2.config(text="Ακολουθείς τα βήματα στο δάσος", command=lambda: self.update_state("forest2"))
            self.button2.pack()  # Show button2
            self.button3.pack_forget()  # Show button3
        elif state == "death2":
            self.story_text.set(
                "Περπατάς για περίπου δέκα δευτερόλεπτα αλλά δυστυχώς "
                "υπάρχει ένα κενό μπροστά που δεν κατάφερες να δεις ποτέ. Το σκοτάδι σε τράβηξε "
                "και έπειτα βυθίστηκες στην αιώνια λήθη."
            )
            self.update_image("hole.jpg")
            self.play_sound("falling.wav")
            self.button1.config(text="Τέλος παιχνιδιού", command=lambda: self.update_state("end"))
            self.button2.config(text="Προσπάθησε ξανά", command=lambda: self.update_state("basement-inside"))
            self.button2.pack()
            self.button3.pack_forget()
        elif state == "lighthouse_top":
            self.story_text.set(
                "Κάθε βήμα στην σκάλα μοίαζει και πιο δύσκολο. Όσο φτάνεις προς την κορυφή "
                "νιώθεις την αναπνοή σου και πιο βαριά. Φτάνεις στο τελευταίο σκαλί "
                "και βλέπεις μία λάμψη που σε τυφλώνει. "
                "Δυστυχώς χάνεις την ισορροπία σου και πέφτεις στο πάτωμα, "
                "αφήνοντας εκεί την τελευταία σου πνοή."

            )
            self.update_image("falling.jpg")
            self.play_sound("falling.wav")
            self.button1.config(text="Τέλος παιχνιδιού", command=lambda: self.update_state("end"))
            self.button2.config(text="Προσπάθησε ξανά", command=lambda: self.update_state("start"))
            self.button3.pack_forget()
            self.button2.pack()
        elif state == "end":
            self.story_text.set(
                "Game over"
            )
            self.update_image("game-over.jpg")
            self.play_sound("game-over.wav")
            self.window.after(4000, self.window.destroy)
            self.button1.pack_forget()
            self.button2.pack_forget()
            self.button3.pack_forget()
# Run the game
if __name__ == "__main__":
    AdventureGame()