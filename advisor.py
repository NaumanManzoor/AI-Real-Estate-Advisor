import openai
import gradio as gr


openai.api_key = "sk....asnj"  # Replace with your actual API key

messages = [{"role": "system", "content": "You are a financial expert specializing in real estate investment and negotiation."}]

def custom_chatgpt(query):
    try:
        messages.append({"role": "user", "content": query})
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Change to appropriate model
            prompt=messages,
            max_tokens=150  # Adjust max tokens based on your needs
        )
        reply = response['choices'][0]['text'].strip()
        messages.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {str(e)}"  # Catch and return any errors that occur

# Build Gradio UI with theme toggling (light/dark)
with gr.Blocks(css="style.css") as demo:

    gr.Markdown("# 🏘️ Real Estate Pro\nYour AI advisor for property investment & negotiation tips.")

    with gr.Row():
        user_input = gr.Textbox(lines=3, placeholder="Ask your real estate question here...", label="💬 Your Question")
        output = gr.Textbox(lines=5, label="🤖 Expert Response")

    with gr.Row():
        submit_btn = gr.Button("💡 Get Advice")
        clear_btn = gr.Button("🧹 Clear")
        toggle_btn = gr.Button("🌓 Toggle Theme")

    submit_btn.click(fn=custom_chatgpt, inputs=user_input, outputs=output)
    clear_btn.click(lambda: ("", ""), None, [user_input, output])

    def toggle_theme():
        current_class = gr.HTML.get_body_class()
        if current_class == "light":
            new_class = "dark"
        else:
            new_class = "light"
        gr.HTML.set_body_class(new_class)

    toggle_btn.click(fn=toggle_theme)

demo.launch(share=True)
