# Project Title

This project provides resources and learning objectives related to web servers and domain name system (DNS).

## Resources

Read or watch:

- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://nginx.org/en/docs/)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-configure-nginx)
- [Child process concept page](https://en.wikipedia.org/wiki/Child_process)
- [Root and sub domain](https://en.wikipedia.org/wiki/Subdomain#Root_domain)
- [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [HTTP redirection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections)
- [Not found HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)
- [Logs files on Linux](https://www.loggly.com/ultimate-guide/linux-logging-basics/)
  
For reference:

- [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://tools.ietf.org/html/rfc7540)

man or help:

- scp
- curl

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

### DNS

- What DNS stands for
- What is DNS main role
- DNS Record Types:
  - A
  - CNAME
  - TXT
  - MX

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing
- You can’t use `systemctl` for restarting a process