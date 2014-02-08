# revision 26786
# category Package
# catalog-ctan /macros/latex/contrib/nolbreaks
# catalog-date 2012-06-01 11:46:45 +0200
# catalog-license pd
# catalog-version 1.2
Name:		texlive-nolbreaks
Version:	1.2
Release:	2
Summary:	No line breaks in text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nolbreaks
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nolbreaks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nolbreaks.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 812683
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754353
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719125
- texlive-nolbreaks
- texlive-nolbreaks
- texlive-nolbreaks
- texlive-nolbreaks

