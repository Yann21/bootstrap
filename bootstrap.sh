#!/usr/bin/env bash
set -e

if ! [ -x "$(command -v ansible)" ]; then
    sudo pacman -S ansible
fi

export ANSIBLE_NOCOWS=1

# Install pacman plugin for Ansible
ansible-galaxy collection install community.general

# Run playbook
ansible-playbook playbook.yml -i hosts --ask-become-pass

if command -v terminal-notifier 1> /dev/null 2>&1; then
    terminal-notifier -title "dotfiles: Bootstrap complete" -message "Successfully set up dev environment."
fi
