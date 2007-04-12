
%define name	voikko-fi
%define tarname	suomi-malaga
%define dirname	suomimalaga
%define version	0.7.4
%define rel	1

Summary:	Description of Finnish morphology written in Malaga (Voikko edition)
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPL
Group:		Text tools
URL:            http://voikko.sourceforge.net/
Source:         http://downloads.sourceforge.net/voikko/%tarname-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	malaga
Requires:	locales-fi
Provides:	voikko-dictionary
Provides:	voikko-fi_FI
Provides:	spell-fi
Provides:	suomi-malaga-voikko
Obsoletes:	suomi-malaga-voikko

%description
Description of Finnish morphology written in Malaga. This version is modified
to support the Voikko spellchecker/hyphenator and is not compatible with the
Sukija text indexer.

%prep
%setup -q -n %dirname-%version

# Enable the IT special dictionary unconditionally for now.
# This should likely be dropped when these become configurable at run-time.
cat sanat/erikoisalat/atk.lex >> sanat/omat.lex

%build
%make voikko

%install
rm -rf %{buildroot}

# Files differ on big-endian and small-endian archs, and they have different
# names (*_l vs *_b). This is the reason we use %{_prefix}/lib instead of
# %{_datadir} and won't noarch the package. Note that we use %{_prefix}/lib
# instead of %{_libdir} to achieve biarch compatibility. That is, if the user
# has both libvoikkoX and lib64voikkoX installed, both of them work with the
# same voikko-fi package.
install -d -m755 %{buildroot}%{_prefix}/lib/voikko
install -m644 voikko-fi_FI*_[lb] voikko-fi_FI.pro %{buildroot}%{_prefix}/lib/voikko

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog LUE.MINUT ohjeet
%{_prefix}/lib/voikko



