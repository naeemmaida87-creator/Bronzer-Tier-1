# Personal AI Employee - Bronze Tier

> Hackathon 0: Building Autonomous FTEs in 2026

## What is this?
A local-first Personal AI Employee that monitors folders, creates tasks automatically,
and uses Claude Code to process them.

## Architecture
Drop_Here → filesystem_watcher.py → Needs_Action → Claude Code → Dashboard updated → Done

## Tech Stack
- Brain: Claude Code
- Dashboard: Obsidian
- Watcher: Python + Watchdog
- OS: Windows 11

## Folder Structure
- Needs_Action/ — Pending tasks
- Plans/ — Claude generated plans
- Done/ — Completed tasks
- Logs/ — Audit trail
- Pending_Approval/ — Human approval needed
- Drop_Here/ — Drop files to trigger AI

## Setup
pip install watchdog
python filesystem_watcher.py

## Bronze Tier Checklist
- [x] Obsidian vault with Dashboard.md and Company_Handbook.md
- [x] Working File System Watcher script
- [x] Claude Code reading and writing to vault
- [x] Basic folder structure complete

## Hackathon Submission
- Tier: Bronze
- Submit: https://forms.gle/JR9T1SJq5rmQyGkGA
