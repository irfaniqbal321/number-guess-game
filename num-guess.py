import streamlit as st
import random

# Initialize session state variables if they don't exist
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = float('inf')

def reset_game():
    min_num = st.session_state.min_range
    max_num = st.session_state.max_range
    st.session_state.random_number = random.randint(min_num, max_num)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Set up the main UI
st.title("🎮 Number Guessing Game")
st.write("Try to guess the secret number!")

# Game settings sidebar
with st.sidebar:
    st.header("Game Settings")
    
    # Custom range settings
    st.subheader("Number Range")
    col1, col2 = st.columns(2)
    with col1:
        min_range = st.number_input("Min", value=1, key="min_range")
    with col2:
        max_range = st.number_input("Max", value=100, key="max_range")
    
    # Difficulty settings
    difficulty = st.selectbox(
        "Select Difficulty",
        ["Easy", "Medium", "Hard", "Custom"],
        key="difficulty"
    )
    
    if difficulty == "Easy":
        st.session_state.max_attempts = 10
    elif difficulty == "Medium":
        st.session_state.max_attempts = 7
    elif difficulty == "Hard":
        st.session_state.max_attempts = 5
    else:  # Custom
        st.session_state.max_attempts = st.number_input("Max Attempts", value=10, min_value=1)
    
    if st.button("New Game"):
        reset_game()

# Main game interface
if not st.session_state.game_over:
    guess = st.number_input(
        "Enter your guess:",
        min_value=st.session_state.min_range,
        max_value=st.session_state.max_range,
        key="guess"
    )
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if guess == st.session_state.random_number:
            st.success(f"🎉 Congratulations! You found the number in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True
        elif st.session_state.attempts >= st.session_state.max_attempts:
            st.error(f"Game Over! You've reached the maximum number of attempts. The number was {st.session_state.random_number}.")
            st.session_state.game_over = True
        elif guess < st.session_state.random_number:
            st.warning("Too low! Try a higher number.")
        else:
            st.warning("Too high! Try a lower number.")

# Display game statistics
st.sidebar.markdown("---")
st.sidebar.subheader("Game Statistics")
st.sidebar.write(f"Attempts: {st.session_state.attempts}")
st.sidebar.write(f"Max Attempts: {st.session_state.max_attempts}")
st.sidebar.write(f"Number Range: {st.session_state.min_range} to {st.session_state.max_range}")
