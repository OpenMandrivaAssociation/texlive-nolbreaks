Name:		texlive-nolbreaks
Version:	26786
Release:	2
Summary:	No line breaks in text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nolbreaks
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nolbreaks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nolbreaks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Use \nolbreaks{some text} to prevent line breaks in "some
text". This has the advantage over \mbox{} that glue (rubber
space) remains flexible. Most common cases are handled here
(\linebreak is disabled, for example) but spaces hidden in
macros or { } can still create break-points.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nolbreaks/nolbreaks.sty
%doc %{_texmfdistdir}/doc/latex/nolbreaks/nolbreaks.pdf
%doc %{_texmfdistdir}/doc/latex/nolbreaks/nolbreaks.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
