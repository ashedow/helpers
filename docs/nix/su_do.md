# su vs sudo

Sudo and su are two different ways to gain root privileges (run commands with root permissions). Each functions in a different way, and different Linux distributions use different configurations by default.

## Su

The `su` command allows you to **s**wtich **u**ser and run your commands as some other user under their user ID.

Root user – when you execute it with no additional options. You can use it to switch to any user account type `su bob` command, you’ll be prompted to enter Bob’s password and the shell will switch to Bob’s user account.

While it is not required that the ‘-‘ be specified, it is recommended for an interactive shell. If we switch user without specifying `-` the path or current working directory of /root are not changed, which may cause problems when user1 goes to run commands.

We don’t just have to enter a shell of the new user, we can optionally execute commands as that user with the `-`c flag.

## Sudo

The **s**uper **u**ser **d**o, or `sudo` command on the other hand instead allows you to run a command as root from your current user. By default this will require you to provide your password again as a security measure.

The non root user account requires sudo privileges to do this, and this is normally setup by either adding the user or group to the /etc/sudoers file, or by adding the user to the wheel group.

We can also use sudo in combination with the su command to enter an interactive root shell: `sudo su -`
> This command is essentially the same as just running su in the shell. Instead of telling the system to “switch users” directly, you’re telling it to run the “su” command as root. When sudo su is run, “.profile,” “.bashrc” and “/etc/profile” will be started, much like running su (or su root). This is because if any command is run with sudo in front of it, it’s a command that is given root privileges.

Similarly, we can get a shell with the -`i` flag: `sudo -i`
>Using sudo -i is virtually the same as the sudo su command. Users can gain root by “sudo” and not by switching to the root user. Much like sudo su, the -i flag allows a user to get a root environment without having to know the root account password. sudo -i is also very similar to using sudo su in that it’ll read all of the environmental files (.profile, etc.) and set the environment inside the shell with it.
>
> Where it differs from “sudo su” is that sudo -i is a much cleaner way of gaining root and a root environment without directly interacting with the root user. How? With sudo su you’re using more than one root setuid commands. This fact makes it much more challenging to figure out what environmental variables will be kept and which ones will be changed (when swamping to the root environment). This is not true with sudo -i, and it is because of this most people view it as the preferred method to gain root without logging in directly.

`sudo -s`
The -s switch for “sudo” command reads the $SHELL variable of the current user executing commands. This command works as if the user is running sudo /bin/bash. Sudo -s is a “non-login” style shell. This means that unlike a command like sudo -i or sudo su, the system will not read any environmental files. This means that when a user tells the shell to run sudo -s, it gains root but will not change the user or the user environment. Your home will not be the root home, etc.

## Differences

A major key difference is who gets the root password. If a user wishes to su to root then they require the password of the root account. If instead the user is executing a command with sudo, they only need their own password and sudo privileges. Therefore if you have multiple users that require root privileges on a system, providing sudo access is considered to be more secure as we can audit commands that have been executed by specific users without sharing the root user’s password with other people.

By default a non root user could use sudo privileges to change the root password, however the /etc/sudoers file can be used to only grant root access to specific commands that the user needs to run as root rather than being able to run anything as root. With sudo we can define security policy, allowing one group of users to perform only a specific subset of clearly defined commands as the root user.


## Links
