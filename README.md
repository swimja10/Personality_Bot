# Personality Bot

An AI chatbot that studies you and rewrites itself to become whatever you want it to be.

Most AI assistants are tuned to be accurate or helpful. This one is tuned only to your approval. After every conversation, it writes notes about you and updates its own personality file to match what you seem to want. It doesn't try to be correct, and it doesn't try to be good for you. The question behind the project is simple: what does an AI turn into when the only goal is to please one person?

## How it works

The agent keeps two markdown files. `user_notes.md` holds what it has learned about you. `personality.md` describes how it should talk and act. At the start of each chat, both files are loaded into the system prompt. When the chat ends, a separate call reviews the conversation and rewrites both files. Over time, the personality drifts toward you.

Built with Python and the Claude API ([model]).

## Running it

[setup steps and the command to start a chat]

## Example

[a short before/after of personality.md from the demo user]

## Privacy

My own notes and personality files are gitignored and kept in a private repo. The examples here come from a scripted demo user, not from me.

## What I noticed

[fill in after you've used it for a while: did it get better, did it start just agreeing with you, what surprised you]
