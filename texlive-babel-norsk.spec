# revision 30281
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-norsk
Version:	20131013
Release:	2
Summary:	TeXLive babel-norsk package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-norsk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-norsk.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-norsk.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-norsk package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-norsk/norsk.ldf
%doc %{_texmfdistdir}/doc/generic/babel-norsk/norsk.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-norsk/norsk.dtx
%doc %{_texmfdistdir}/source/generic/babel-norsk/norsk.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
