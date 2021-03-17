#!/usr/bin/bash
pwd=hi
sed -r 's/\$SCRIPTS/${pwd}/g' etc/yeelight.service > here
cp etc/yeelight.service ${HOME}/.config/systemd/user/

systemctl --user enable --now yeelight.service
