# revision 18127
# category Package
# catalog-ctan /macros/latex/contrib/nolbreaks
# catalog-date 2010-05-11 12:36:30 +0200
# catalog-license pd
# catalog-version 1.0
Name:		texlive-nolbreaks
Version:	1.0
Release:	1
Summary:	No line breaks in text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nolbreaks
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nolbreaks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nolbreaks.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Use \nolbreaks{some text} to prevent line breaks in "some
text". This has the advantage over \mbox{} that glue (rubber
space) remains flexible. Most common cases are handled here
(\linebreak is disabled, for example) but spaces hidden in
macros or { } can still create break-points.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nolbreaks/nolbreaks.sty
%doc %{_texmfdistdir}/doc/latex/nolbreaks/nolbreaks.pdf
%doc %{_texmfdistdir}/doc/latex/nolbreaks/nolbreaks.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
