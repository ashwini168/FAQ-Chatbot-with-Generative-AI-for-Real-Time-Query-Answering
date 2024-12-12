from pyngrok import ngrok

# Open ngrok tunnel on port 8501 (Streamlit's default port)
public_url = ngrok.connect(8501)
print(f"Streamlit app is live at: {public_url}")

# Run Streamlit in the background
!streamlit run app.py &
