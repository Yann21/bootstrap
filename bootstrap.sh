#!/usr/bin/env bash
set -e

if ! [ -x "$(command -v ansible)" ]; then
    sudo pacman -S ansible
fi

# Install pacman plugin for Ansible
ansible-galaxy collection install community.general

# Run playbook
ansible-playbook -i playbook.yml --ask-become-pass

if command -v terminal-notifier 1> /dev/null 2>&1; then
    terminal-notifier -title "dotfiles: Bootstrap complete" -message "Successfully set up dev environment."
fi


