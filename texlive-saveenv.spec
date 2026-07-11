%global tl_name saveenv
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.1
Release:	%{tl_revision}.1
Summary:	Save environment content verbatim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/saveenv
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/saveenv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/saveenv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(precattl)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides tools to create your own verbatim environments,
and works for all values of \endlinechar.

