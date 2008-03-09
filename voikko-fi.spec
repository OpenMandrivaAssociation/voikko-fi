
%define name	voikko-fi
%define tarname	suomi-malaga
%define version	1.0
%define rel	2

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
BuildRequires:	python
Requires:	locales-fi
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 3
Provides:	voikko-dictionary
Provides:	voikko-fi_FI
Provides:	spell-fi
Obsoletes:	suomi-malaga-voikko

%description
Description of Finnish morphology written in Malaga. This version is modified
to support the Voikko spellchecker/hyphenator and is not compatible with the
Sukija text indexer.

%prep
%setup -q -n %tarname-%version

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
make voikko-install DESTDIR=%{buildroot}%{_prefix}/lib/voikko

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README README.fi ChangeLog CONTRIBUTORS
%{_prefix}/lib/voikko

