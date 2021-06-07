# difference between /sbin/nologin and /bin/false

`/bin/false` is a system command that is used anytime you need to pass a command to a program that should do nothing more than exit with an error. It's the companion to `/bin/true`. Both of these are very old and standard POSIX utilities and neither produce any output by definition. true is sometimes used for a shell script that should loop indefinitely, like:
```bash
while true; do
    ...
    # Waste time
    if [ $wasted_time -gt 100000 ]; then
        exit 0
    fi
    ...
done
```

`/usr/sbin/nologin` is specifically designed to replace a shell and produces output complaining you can't log-in. Before it existed, it was common to use `/bin/false` for dummy users, but could be confusing since the user doesn't know why they're kicked off.

***

Why do some system users have /usr/bin/false as their shell?

This helps to prevent users from logging onto a system. Sometimes you need a user account for a specific task. Nevertheless, no one should be able to interact with this account on the computer. These are, on one hand, system user accounts. On the other hand, this is an account for which FTP or POP3 access is possible, but just no direct shell login.

If you look more closely at the /etc/passwd file, you will find the /bin/false command as a login shell for many system accounts. Actually, false is not a shell, but a command that does nothing and then also ends with a status code that signals an error. The result is simple. The user logs in and immediately sees the login prompt again.

***

What will happen if
```bash
а=$(pwd)
```

***

How to set keys in a bash scripts

***

What is `case`

***

How will you fix if someone went to the server and executed the following command:
```bash
sudo chmod -x use/bin/chmod
```

