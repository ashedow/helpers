# POSIX

POSIX - Portable Operating System Interface for UNIX. It is a family of standards, specified by the (IEEE)[https://www.ieee.org/], to clarify and make uniform the application programming interfaces (and ancillary issues, such as commandline shell utilities) provided by Unix-y operating systems. 

When you write your programs to rely on POSIX standards, you can be pretty sure to be able to port them easily among a large family of Unix derivatives (including Linux, but not limited to it!); if and when you use some Linux API that's not standardized as part of Posix, you will have a harder time if and when you want to port that program or library to other Unix-y systems (e.g., MacOSX) in the future.

Initially, POSIX was divided into multiple standards:

POSIX.1: Core Services
POSIX.1b: Real-time extensions
POSIX.1c: Threads extensions
POSIX.2: Shell and Utilities

## Basics of POSIX

1. **Base Definition Volume**: General terms, concepts, and interfaces.
2. **Systems Interfaces Volume**: Definitions of system service functions and subroutines. Also, includes portability, error handling and error recovery.
3. **Shell and Utilities Volume**: Definition of interfaces of any application to command shells and common utility programs.
4. **Rationale Volume**: Contains information and history about added or discarded features and the reasonings of the decisions.

> The standard doesn’t cover graphical interfaces, database interfaces, object/binary code portability, system configurations, I/O considerations or resource availability.

### Principles behind POSIX design are:

* POSIX is created to make application portability easier. So it’s not for UNIX systems only. Non-UNIX systems can be POSIX-compliant too.
* The standard doesn’t dictate the development of the application or the operating system. It only defines the contract between them.
* POSIX-compliant application source code should be able to run across many systems because the standard is defined at the source code level. However, the standard doesn’t guarantee any object or binary code level portability. So the binary executable may not run even on similar machines with identical hardware and operating systems. Only source code portability is addressed in the standard.
* POSIX is written in terms of Standard C. But developers can implement it in any language they like.
* The standard only deals with aspects of the operating system that interacts with applications.
* The standard is kept succinct in terms of length and broad in terms of scope to cover a large array of systems.
* POSIX was designed to simplify portability. So it will save time and money in the long run. However, if your applications are not POSIX-compliant, it might require significant time and resource investment at the beginning.

## The most important things POSIX defines

1. (**C API**)[https://pubs.opengroup.org/onlinepubs/9699919799/functions/contents.html]

Greatly extends ANSI C with things like:
* more file operations: `mkdir`, `dirname`, `symlink`, `readlink`, `link` (`hardlinks`), `poll()`, `stat`, `sync`, `nftw()`
* process and threads: `fork`, `execl`, `wait`, `pipe`, semaphors `sem_*`, shared memory (`shm_*`), `kill`, scheduling parameters (`nice`, `sched_*`), `sleep`, `mkfifo`, `setpgid()`
* networking: `socket()`
* memory management: `mmap`, `mlock`, `mprotect`, `madvise`, `brk()`
* utilities: regular expressions (`reg*`)

Those APIs also determine underlying system concepts on which they depend, e.g. `fork` requires a concept of a process.

Many Linux system calls exist to implement a specific POSIX C API function and make Linux compliant, e.g. `sys_write`, `sys_read`, ... Many of those syscalls also have Linux-specific extensions however.

Major Linux desktop implementation: `glibc`, which in many cases just provides a shallow wrapper to system calls.

2. (**CLI utilities**)[https://pubs.opengroup.org/onlinepubs/9699919799/utilities/contents.html]

E.g.: `cd`, `ls`, `echo`, ...

Many utilities are direct shell front ends for a corresponding C API function, e.g. `mkdir`.

Major Linux desktop implementation: GNU Coreutils for the small ones, separate GNU projects for the big ones: sed, grep, awk, ... Some CLI utilities are implemented by Bash (as built-ins)[https://unix.stackexchange.com/questions/11454/what-is-the-difference-between-a-builtin-command-and-one-that-is-not].

3. (**Shell language**)[https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18]

E.g., `a=b`; `echo "$a"`

Major Linux desktop implementation: (GNU Bash)[https://www.gnu.org/software/bash/].

4. (**Environment variables**)[https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html#tag_08]

E.g.: `HOME`, `PATH`.

`PATH` search semantics are specified, including how slashes prevent PATH search.

5. (**Program exit status**)[https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_08]

ANSI C says `0` or `EXIT_SUCCESS` for success, `EXIT_FAILURE` for failure, and leaves the rest implementation defined.

POSIX adds:

* `126`: command found but not executable.
* `127`: command not found.
* `> 128`: terminated by a signal.

But POSIX does not seem to specify the `128 + SIGNAL_ID` rule used by Bash: https://unix.stackexchange.com/questions/99112/default-exit-code-when-process-is-terminated

6. (**Regular expression**)[https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09]

There are two types: BRE (Basic) and ERE (Extended). Basic is deprecated and only kept to not break APIs.

Those are implemented by C API functions, and used throughout CLI utilities, e.g. grep accepts BREs by default, and EREs with `-E`.

E.g.: `echo 'a.1' | grep -E 'a.[[:digit:]]'`

Major Linux implementation: glibc implements the functions under regex.h which programs like `grep` can use as backend.

7. (**Directory structure**)[https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap10.html#tag_10]

E.g.: `/dev/null`, `/tmp`

The Linux FHS(Filesystem Hierarchy Standard
) greatly extends POSIX.

8. (**Filenames**)[https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_267]

* `/` is the path separator
* `NUL` cannot be used
* `.` is `cwd`, `..` parent
* portable filenames
    * use at most max 14 chars and 256 for the full path
    * can only contain: `a-zA-Z0-9._-`

9. (**Command line utility API conventions**)[https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html]

Not mandatory, used by POSIX, but almost nowhere else, notably not in GNU. But true, it is too restrictive, e.g. single letter flags only (e.g. -a), no double hyphen long versions (e.g. --all).

A few widely used conventions:
    * `-` means stdin where a file is expected
    * `--` terminates flags, e.g. `ls -- -l` to list a directory named `-l`
See also: Are there standards for Linux command line switches and arguments?

10. **"POSIX ACLs" (Access Control Lists), e.g. as used as backend for `setfacl`.**

This was withdrawn but it was implemented in several OSes, including in Linux with `setxattr`.

## Who conforms to POSIX?

Many systems follow POSIX closely, but few are actually certified by the Open Group which maintains the standard. Notable certified ones include:

OS X (Apple) X stands for both 10 and UNIX. Was the first Apple POSIX system, released circa 2001. See also: Is OSX a POSIX OS?
AIX (IBM)
HP-UX (HP)
Solaris (Oracle)
Most Linux distros are very compliant, but not certified because they don't want to pay the compliance check. Inspur's K-UX and Huawei's EulerOS are two certified examples.

The official list of certified systems be found at: https://www.opengroup.org/openbrand/register/ and also at the wiki page.

**Windows**

Windows implemented POSIX on some of its professional distributions.
Since it was an optional feature, programmers could not rely on it for most end user applications.
Support was deprecated in Windows 8

Historical overview of the official Microsoft POSIX compatibility: http://brianreiter.org/2010/08/24/the-sad-history-of-the-microsoft-posix-subsystem/

Cygwin is a well known GPL third-party project for that "provides substantial POSIX API functionality" for Windows, but requires that you "rebuild your application from source if you want it to run on Windows". MSYS2 is a related project that seems to add more functionality on top of Cygwin.

**Android**

Android has its own C library (Bionic) which does not fully support POSIX as of Android O.

**Bonus level**

The Linux Standard Base further extends POSIX.

Use the non-frames indexes, they are much more readable and searchable: http://pubs.opengroup.org/onlinepubs/9699919799/nfindex.html
## 