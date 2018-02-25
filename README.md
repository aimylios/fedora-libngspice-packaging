# Packaging the ngspice shared libraries for Fedora

Ngspice is a general-purpose circuit simulation program for nonlinear and linear analyses. Please visit the [official ngspice website](http://ngspice.sourceforge.net/) for details.

As of February 2018 the [Fedora ngspice package](https://src.fedoraproject.org/rpms/ngspice) does not include the shared libraries (see RedHat Bugzilla [#1440904](https://bugzilla.redhat.com/show_bug.cgi?id=1440904) and [#1492481](https://bugzilla.redhat.com/show_bug.cgi?id=1492481) for details). This makes it difficult to build and install software that requires libngspice.

As a workaround I decided to build my own libngspice RPM, just including the shared libraries and extending the upstream package. This is not the optimal solution, but should be sufficient for my personal needs. I did some testing with the current development version of [KiCad](http://kicad-pcb.org/) (which supports simulation based on libngspice) and could not find any issues.

This repository only includes the SPEC description file for the libngspice RPM, the ngspice source itself can be found at [Sourceforge]((http://ngspice.sourceforge.net/)). A ready-made RPM is included in my personal [aimylios/electronics](https://copr.fedorainfracloud.org/coprs/aimylios/electronics/) Copr repository.
