#!/usr/bin/env bash
set -e

# Install ansible on new machine
if ! [ -x "$(command -v ansible)" ]; then
    sudo pacman -S ansible
fi

export ANSIBLE_NOCOWS=1

# Install Ansible plugins
ansible-galaxy collection install community.general
ansible-galaxy install kewlfft.aur

# Run playbook
ansible-playbook playbook.yml -i hosts --ask-become-pass

# Notify
if command -v terminal-notifier 1> /dev/null 2>&1; then
    terminal-notifier -title "dotfiles: Bootstrap complete" -message "Successfully set up dev environment."
fi
