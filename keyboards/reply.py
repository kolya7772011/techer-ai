from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from utils.constants import Subject, LearningStyle, TOPIC_MAP


class Keyboards:
    """Keyboard generators."""
    
    @staticmethod
    def main_menu() -> ReplyKeyboardMarkup:
        """Main menu keyboard."""
        buttons = [
            [KeyboardButton("📚 Dars"), KeyboardButton("👤 Profil")],
            [KeyboardButton("🏆 Lider doska"), KeyboardButton("⚙️ Sozlamalar")],
        ]
        return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    
    @staticmethod
    def subjects_inline() -> InlineKeyboardMarkup:
        """Subjects selection keyboard."""
        buttons = []
        for subject in Subject:
            buttons.append([InlineKeyboardButton(subject.value, callback_data=f"subject_{subject.name}")])
        return InlineKeyboardMarkup(buttons)
    
    @staticmethod
    def topics_inline(subject: str) -> InlineKeyboardMarkup:
        """Topics for selected subject."""
        topics = TOPIC_MAP.get(subject, [])
        buttons = []
        for topic in topics:
            callback_data = f"topic_{topic.replace(' ', '_')}"
            buttons.append([InlineKeyboardButton(topic, callback_data=callback_data)])
        buttons.append([InlineKeyboardButton("◀️ Orqaga", callback_data="back_to_subjects")])
        return InlineKeyboardMarkup(buttons)
    
    @staticmethod
    def learning_styles_inline() -> InlineKeyboardMarkup:
        """Learning styles selection."""
        buttons = []
        styles_info = {
            LearningStyle.VISUAL: "👁️ Visual",
            LearningStyle.AUDITORY: "👂 Auditory",
            LearningStyle.READING: "📖 Reading",
            LearningStyle.PRACTICE: "✍️ Practice",
        }
        for style, label in styles_info.items():
            buttons.append([InlineKeyboardButton(label, callback_data=f"style_{style.name}")])
        return InlineKeyboardMarkup(buttons)
    
    @staticmethod
    def confirmation_inline() -> InlineKeyboardMarkup:
        """Confirmation buttons."""
        buttons = [
            [InlineKeyboardButton("✅ Ha", callback_data="confirm_yes"),
             InlineKeyboardButton("❌ Yo'q", callback_data="confirm_no")]
        ]
        return InlineKeyboardMarkup(buttons)
    
    @staticmethod
    def class_selection_inline() -> InlineKeyboardMarkup:
        """Class selection keyboard."""
        buttons = []
        for i in range(1, 12):
            class_name = f"{i}-sinf"
            buttons.append([InlineKeyboardButton(class_name, callback_data=f"class_{i}")])
        return InlineKeyboardMarkup(buttons)
    
    @staticmethod
    def settings_menu() -> InlineKeyboardMarkup:
        """Settings menu."""
        buttons = [
            [InlineKeyboardButton("🔔 Eslatma", callback_data="settings_reminder")],
            [InlineKeyboardButton("📚 Fan o'zgartirish", callback_data="settings_subject")],
            [InlineKeyboardButton("👤 Stil o'zgartirish", callback_data="settings_style")],
            [InlineKeyboardButton("◀️ Orqaga", callback_data="back_to_menu")],
        ]
        return InlineKeyboardMarkup(buttons)
    
    @staticmethod
    def reminder_settings_inline() -> InlineKeyboardMarkup:
        """Reminder settings."""
        buttons = [
            [InlineKeyboardButton("✅ Yoqish", callback_data="reminder_on"),
             InlineKeyboardButton("❌ O'chirish", callback_data="reminder_off")],
            [InlineKeyboardButton("⏰ Vaqt o'zgartirish", callback_data="reminder_time")],
            [InlineKeyboardButton("◀️ Orqaga", callback_data="back_to_settings")],
        ]
        return InlineKeyboardMarkup(buttons)
