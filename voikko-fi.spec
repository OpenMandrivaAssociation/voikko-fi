
%define tarname	suomi-malaga
%define prever	0
%define rel	5

Summary:	Finnish support for Voikko spellchecker/hyphenator
Name:		voikko-fi
Version:	1.8
%if %{prever}
Release:	2.%{prever}.%{rel}
%else
Release:	%{rel}
%endif
License:	GPLv2+
Group:		Text tools
URL:            http://voikko.sourceforge.net/
%if %prever
Source:		http://www.puimula.org/htp/testing/%tarname-%version%prever.tar.gz
%else
Source:         http://downloads.sourceforge.net/voikko/%tarname-%version.tar.gz
%endif
BuildRequires:	malaga >= 7.8
BuildRequires:	python2
Requires:	locales-fi
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 3
Provides:	voikko-dictionary
Provides:	voikko-fi_FI
Provides:	spell-fi
Obsoletes:	suomi-malaga-voikko < 1.0
BuildArch:	noarch

%description
Description of Finnish morphology written in Malaga. This version is modified
to support the Voikko spellchecker/hyphenator and is not compatible with the
Sukija text indexer.

%prep
%setup -q -n %{tarname}-%{version}

%build
# (tpg) build with py2
sed -i -e "s/PYTHON=python/PYTHON=%{__python2}/g" Makefile

%make voikko GENLEX_OPTS="--extra-usage=it" \
	EXTRA_LEX="vocabulary/erikoisalat/linux-distributions.lex vocabulary/erikoisalat/atk-lyhenteet.lex"

%install
# Files differ on big-endian and small-endian archs, and they have different
# names (*_l vs *_b). This is the reason we use %{_prefix}/lib instead of
# %{_datadir} and won't noarch the package. Note that we use %{_prefix}/lib
# instead of %{_libdir} to achieve biarch compatibility. That is, if the user
# has both libvoikkoX and lib64voikkoX installed, both of them work with the
# same voikko-fi package.
make voikko-install DESTDIR=%{buildroot}%{_prefix}/lib/voikko

%files
%doc README README.fi CONTRIBUTORS
%dir %{_prefix}/lib/voikko
%{_prefix}/lib/voikko/?


%changelog
* Fri Apr 22 2011 Anssi Hannula <anssi@mandriva.org> 1.8-1mdv2011.0
+ Revision: 656759
- new version 1.8
- sync Summary from Mageia

* Sat Oct 02 2010 Anssi Hannula <anssi@mandriva.org> 1.7-1mdv2011.0
+ Revision: 582508
- new version

* Sat Jul 10 2010 Anssi Hannula <anssi@mandriva.org> 1.6-1mdv2011.0
+ Revision: 549976
- new version

* Sat Feb 06 2010 Anssi Hannula <anssi@mandriva.org> 1.5-1mdv2010.1
+ Revision: 501393
- new version

* Thu Oct 01 2009 Anssi Hannula <anssi@mandriva.org> 1.4-1mdv2010.0
+ Revision: 452158
- new version (no changes since 1.4rc3)

* Sun Sep 27 2009 Anssi Hannula <anssi@mandriva.org> 1.4-0.rc3.1mdv2010.0
+ Revision: 449967
- new version 1.4rc3

* Sat Sep 19 2009 Anssi Hannula <anssi@mandriva.org> 1.4-0.rc2.1mdv2010.0
+ Revision: 444709
- new testing release 1.4rc2

* Sun Jul 19 2009 Anssi Hannula <anssi@mandriva.org> 1.3-2mdv2010.0
+ Revision: 397629
- adapt file locations for current libvoikko

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.3-1mdv2009.1
+ Revision: 359196
- new version
- enable special linux distributions vocabulary

* Fri Nov 28 2008 Anssi Hannula <anssi@mandriva.org> 1.2-1mdv2009.1
+ Revision: 307493
- new version
- versionize buildrequires and obsoletes
- enable it vocabulary

* Tue May 13 2008 Anssi Hannula <anssi@mandriva.org> 1.1-1mdv2009.0
+ Revision: 206548
- new version
- apply new license policy

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 1.0-2mdv2008.1
+ Revision: 182392
- provide enchant-dictionary

* Sat Jan 12 2008 Anssi Hannula <anssi@mandriva.org> 1.0-1mdv2008.1
+ Revision: 149672
- update to new version 1.0

* Wed Dec 26 2007 Anssi Hannula <anssi@mandriva.org> 0.7.7-1mdv2008.1
+ Revision: 137922
- 0.7.7

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.7.6-1mdv2008.1
+ Revision: 136571
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 03 2007 Anssi Hannula <anssi@mandriva.org> 0.7.6-1mdv2008.0
+ Revision: 78612
- 0.7.6
- remove upstream patch0
- re-enable parallel make

* Wed May 16 2007 Anssi Hannula <anssi@mandriva.org> 0.7.5-2mdv2008.0
+ Revision: 27290
- P0 from SVN: fix a regression

* Tue May 15 2007 Anssi Hannula <anssi@mandriva.org> 0.7.5-1mdv2008.0
+ Revision: 27048
- 0.7.5


* Mon Feb 19 2007 Anssi Hannula <anssi@mandriva.org> 0.7.4-1mdv2007.0
+ Revision: 122804
- 0.7.4
- enable the special IT dictionary
- update URL

* Sat Nov 11 2006 Anssi Hannula <anssi@mandriva.org> 0.7.3-1mdv2007.1
+ Revision: 83032
- 0.7.3

* Sun Oct 29 2006 Anssi Hannula <anssi@mandriva.org> 0.7.2-1mdv2007.1
+ Revision: 73614
- update tarball
- 0.7.2
- Import voikko-fi

* Tue Aug 22 2006 Anssi Hannula <anssi@mandriva.org> 0.7.1-3mdv2007.0
- rename to voikko-fi
- add some provides
- use voikko upstream dictionary path

* Wed Aug 16 2006 Anssi Hannula <anssi@mandriva.org> 0.7.1-2mdv2007.0
- put files in %%{prefix}/lib to achieve biarch compatibility

* Mon Aug 14 2006 Anssi Hannula <anssi@mandriva.org> 0.7.1-1mdv2007.0
- initial Mandriva release

