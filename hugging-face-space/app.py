from pytube import YouTube
from transformers import pipeline
import gradio as gr
import os

pipe = pipeline(model="almino/checkpoints")

def get_audio(url):
  yt = YouTube(url)
  video = yt.streams.filter(only_audio=True).first()
  out_file=video.download(output_path=".")
  base, ext = os.path.splitext(out_file)
  new_file = base+'.mp3'
  os.rename(out_file, new_file)
  a = new_file
  return a

def get_text(url):
  result = pipe(get_audio(url))['text']
  return result


  
with gr.Blocks() as demo:
  gr.Markdown("<h1><center>Youtube video transcription with OpenAI's Whisper</center></h1>")
  gr.Markdown("<center>Enter the link of any youtube video to get the transcription of the video.</center>")
  with gr.Tab('Get the transcription of any Youtube video'):
    with gr.Row():
      input_text_1 = gr.Textbox(placeholder='Enter the Youtube video URL', label='URL')
      output_text_1 = gr.Textbox(placeholder='Transcription of the video', label='Transcription')
    result_button_1 = gr.Button('Get Transcription')
 

  result_button_1.click(get_text, inputs = input_text_1, outputs = output_text_1)
demo.launch(debug=True)
