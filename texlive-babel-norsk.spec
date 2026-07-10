%global tl_name babel-norsk
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0k
Release:	%{tl_revision}.1
Summary:	Babel support for Norwegian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/norsk
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-norsk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-norsk.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-norsk.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of
Norwegian in babel. Some shortcuts are defined, as well as translations
to Norsk of standard "LaTeX names".

