import streamlit as st
import google.generativeai as genai
#MILESTONE 1 (The Foundation)
# Configure API key
# PASTE YOUR KEY INSIDE THE QUOTES BELOW
api_key = "YOUR_API_KEY_HERE"
genai.configure(api_key=api_key)

# Create the model configuration
generation_config = {
    "temperature": 0.4,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the Generative Model
model = genai.GenerativeModel(
    model_name="gemini-model",
    generation_config=generation_config,
)


#  MILESTONE 3 (The Brain)
def generate_itinerary(destination, days, nights):
    # This matches the "Chat Session" logic from your screenshot
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"write me a travel itinerary to {destination} for {days} days and {nights} nights",
                ],
            }
        ]
    )
    # Send the message
    response = chat_session.send_message(f"Create a detailed travel itinerary for {days} days and {nights} nights in {destination}.")
    return response.text

#  MILESTONE 4 (The Face) 
def main():
    st.title("Travel Itinerary Generator")
    
    # Inputs
    destination = st.text_input("Enter your desired destination:")
    days = st.number_input("Enter the number of days:", min_value=1)
    nights = st.number_input("Enter the number of nights:", min_value=0)
    
    # Button
    if st.button("Generate Itinerary"):
        if destination.strip() and days > 0:
            try:
                # Call the function from Part 2
                itinerary = generate_itinerary(destination, days, nights)
                st.text_area("Generated Itinerary:", value=itinerary, height=300)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please enter a valid destination and days.")

if __name__ == "__main__":

    main()


