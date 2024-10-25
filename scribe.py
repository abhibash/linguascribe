import streamlit as st
import whisper
import ssl
import tempfile
from googletrans import Translator
import time

translator = Translator()
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}

# Bypass SSL verification (if needed)
ssl._create_default_https_context = ssl._create_unverified_context

# Streamlit page configuration
st.set_page_config(page_title="LinguaScribe", page_icon="assets/transcription.png", layout="wide")


# Sidebar for Whisper model selection and instructions
with st.sidebar:
    st.image("assets/transcription.png", width=100)
    st.markdown("## Lingua:blue[Scribe]")

    
    
    # Speed and Accuracy Indicators for each model
    speed = {"tiny": 10, "base": 7, "small": 6, "medium": 4, "large": 2}
    accuracy = {"tiny": 4, "base": 6, "small": 8, "medium": 9, "large": 10}


    
    whisper_model = st.selectbox(
        "# Model Speed & Accurarcy", options=["tiny", "base", "small", "medium", "large"], index=1
    )
    st.markdown(f"**Speed** (Relative):")
    st.progress(speed[whisper_model] / 10.0)
    
    st.markdown(f"**Accuracy** (Relative):")
    st.progress(accuracy[whisper_model] / 10.0)
    
   
    
# Load Whisper model with caching
@st.cache_resource
def load_model(whisper_model):
    return whisper.load_model(whisper_model)

model = load_model(whisper_model)
#st.text("Whisper model loaded")
col1,col2 = st.columns([6,1])
with col1:
    st.header("Lingua:blue[Scribe]")
    st.markdown("Record :blue[:material/arrow_forward:] Transcribe :blue[:material/arrow_forward:] Translate ")
with col2:
    st.markdown("")
    with st.popover("How to use"):
      st.markdown("""
        ### How to Use LinguaScribe:

        Follow these steps to transcribe and translate your audio, with the option to try different models for varying levels of speed and accuracy:

        1. **Upload or Record Audio:**
        - **Upload Audio**: Click the "Upload Audio" option to select an audio file from your device (supports WAV, MP3, M4A).
        - **Record Audio**: Use the "Record Audio" option to record audio directly using your microphone. Start and stop recording by clicking the button.

        2. **Transcribe Audio:**
        - The **default transcription model** is set to `base`, which offers a good balance between speed and accuracy.
        - If you want more accurate results, you can switch to a larger model, like `medium` or `large`, though this may take more time.
        - Click **"Transcribe Audio"** to begin the transcription process. A progress bar will indicate the status.

        3. **Edit the Transcription (if needed):**
        - Once transcription is complete, go to the **Transcription** tab to view the transcribed text.
        - You can manually **edit the transcription** in the text area if necessary, making adjustments for clarity or accuracy before moving forward.

        4. **Translate the Transcription:**
        - In the **Translation** tab, select the target language for translation.
        - Click **"Translate"** to convert the transcription into your selected language. The translated text will appear for review.

        5. **Download Your Work:**
        - After finalizing the transcription and translation, use the **Download** buttons in each tab to save the text files to your device.

        ### Important Notes:
        - **Default Model (Base)**: The application uses the `base` model by default, which balances speed and accuracy. You do not need to change this unless you want to experiment with other models.
        - **Optional Model Selection**: For quicker transcriptions, try the `tiny` model. For more **accurate results**, try `medium` or `large`, but note that larger models will take longer to process.
        - **Editing Transcription**: You can manually edit the transcribed text at any time to improve accuracy or make corrections before translation.
        """)



# Main section: Tabs for Audio Input, Transcription, and Translation
tab1, tab2, tab3 = st.tabs(["Audio Input", "Transcription", "Translation"])

# Tab 1: Audio Input
with tab1:
    st.header("Audio Input")
    choice = st.selectbox(
        "Choose Input Method", ("Upload Audio", "Record Audio"), placeholder="Upload or Record Audio",index=None
    )

    audio_value = None
    if choice == "Upload Audio":
        audio_value = st.file_uploader("Upload an audio file",type=["wav", "mp3", "m4a"])
        if audio_value and audio_value.type.startswith('audio'):
            st.audio(audio_value)
        elif audio_value:
            st.error("Please upload a valid audio file")
    elif choice == "Record Audio":
        recorded_audio = st.experimental_audio_input("Record your audio", help="Hit record again for new audio")
        if recorded_audio:
            audio_value = recorded_audio

    # Progress and Transcription button
    if st.button("Transcribe Audio"):
        if audio_value is not None:
            with st.spinner("Transcribing... Please wait!"):
                progress_bar = st.progress(0)
                for i in range(5):  # Simulate progress steps
                    time.sleep(0.5)
                    progress_bar.progress((i + 1) * 20)
                with tempfile.NamedTemporaryFile(delete=False) as temp_audio_file:
                    temp_audio_file.write(audio_value.read())
                    temp_audio_file_path = temp_audio_file.name

                # Transcribe using Whisper model
                transcription = model.transcribe(temp_audio_file_path)
                st.success("Transcription Complete")
                transcribed_text = transcription["text"]
                st.session_state['transcribed_text'] = transcribed_text
        else:
            st.error("Please upload or record audio")

# Tab 2: Transcription (editable)
with tab2:
    st.header("Transcription")
    if 'transcribed_text' in st.session_state:
        edited_transcribed_text = st.text_area("Edit Transcription", st.session_state['transcribed_text'])
        st.session_state['transcribed_text'] = edited_transcribed_text
    else:
        st.warning("Please transcribe audio first in the Audio Input tab.")
    
    if 'transcribed_text' in st.session_state:
        st.download_button("Download Transcription", st.session_state['transcribed_text'], file_name="transcription.txt")

# Tab 3: Translation
with tab3:
    st.header("Translation")
    if 'transcribed_text' in st.session_state:
        # Show transcription and allow translation
        st.markdown("### Transcribed Text")
        st.markdown(st.session_state['transcribed_text'])
        
        # Language selection and translation
        target_language = st.selectbox("Select Language to Translate To", list(LANGUAGES.values()),index=None)
        if st.button("Translate"):
            with st.spinner("Translating... Please wait!"):
                try:
                    transcribed_text = st.session_state.get('transcribed_text')
                    translated_text = translator.translate(transcribed_text, dest=target_language).text
                    #st.success("Translation Complete")
                    st.markdown("### Translated Text")
                    st.markdown(translated_text)
                    st.session_state['translated_text'] = translated_text
                except Exception as e:
                    st.error(f"An error occurred during translation: {str(e)}")
    else:
        st.warning("Please transcribe audio first in the Audio Input tab.")

    if 'translated_text' in st.session_state:
        st.download_button("Download Translation", st.session_state['translated_text'], file_name="translation.txt")


# Download options (in any tab)
#if 'transcribed_text' in st.session_state:
   # st.download_button("Download Transcription", st.session_state['transcribed_text'], file_name="transcription.txt")

