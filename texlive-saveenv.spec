Name:		texlive-saveenv
Version:	65346
Release:	1
Summary:	Save environment content verbatim
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/saveenv
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/saveenv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/saveenv.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides tools to create your own verbatim
environments, and works for all values of \endlinechar.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/saveenv
%doc %{_texmfdistdir}/doc/latex/saveenv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
