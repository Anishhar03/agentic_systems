# Streamlit Chatbot

## Goal

Add a lightweight UI to an agent workflow.

## Components

- session_state for current thread id.
- chat input for user turns.
- streaming output for model tokens or graph events.
- trace panel for node transitions.
- approval panel for human-in-the-loop actions.

## Production Upgrade

Replace Streamlit session state with a backend API, database-backed checkpointer, authentication, and request tracing.
