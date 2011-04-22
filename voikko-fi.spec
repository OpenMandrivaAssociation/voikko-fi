
%define name	voikko-fi
%define tarname	suomi-malaga
%define version	1.8
%define prever	0
%define rel	1

Summary:	Finnish support for Voikko spellchecker/hyphenator
Name:		%name
Version:	%version
%if %prever
Release:	%mkrel 0.%prever.%rel
%else
Release:	%mkrel %rel
%endif
License:	GPLv2+
Group:		Text tools
URL:            http://voikko.sourceforge.net/
%if %prever
Source:		http://www.puimula.org/htp/testing/%tarname-%version%prever.tar.gz
%else
Source:         http://downloads.sourceforge.net/voikko/%tarname-%version.tar.gz
%endif
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	malaga >= 7.8
BuildRequires:	python
Requires:	locales-fi
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 3
Provides:	voikko-dictionary
Provides:	voikko-fi_FI
Provides:	spell-fi
Obsoletes:	suomi-malaga-voikko < 1.0

%description
Description of Finnish morphology written in Malaga. This version is modified
to support the Voikko spellchecker/hyphenator and is not compatible with the
Sukija text indexer.

%prep
%setup -q -n %tarname-%version

%build
%make voikko GENLEX_OPTS="--extra-usage=it" \
	EXTRA_LEX="vocabulary/erikoisalat/linux-distributions.lex vocabulary/erikoisalat/atk-lyhenteet.lex"

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
%doc README README.fi CONTRIBUTORS
%dir %{_prefix}/lib/voikko
%{_prefix}/lib/voikko/?

