%global fontname   nafees-pakistani-web-naskh
%global fontconf   67-%{fontname}.conf 
Name:		%{fontname}-fonts
Version:	2.0
Release:	2%{?dist}
Summary:	Nafees pakistani web naskh font for writing Urdu 

Group:		User Interface/X	
License:	Bitstream Vera
URL:		http://www.crulp.org/index.htm		
Source0:	http://www.crulp.org/Downloads/NafeesPakistaniWebNaskh(BTK2.0).ttf
Source1:	%{fontname}-update-preferred-family.pe
Source2:	%{fontconf}
Source3:	http://www.crulp.org/Downloads/NafeesPakistaniWebNaskh(BTK2.0).pdf
Source4:	http://www.crulp.org/software/license/Nafees_Pakistani_Naskh_License.html
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	fontforge	
Requires:	fontpackages-filesystem

%description
This font is developed on Unicode standard and is based \
 on Naskh writing style. \
Guidance and calligraphy of basic glyph s for the font \
has been provided by Syed Jameel-ur- Rehman. 

%prep

%build
%{_bindir}/fontforge %{SOURCE1} '%{SOURCE0}'

%install


#fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf

%doc  '%{SOURCE3}' '%{SOURCE4}'


%changelog
* Fri Sep 09 2011 Anish Patil <apatil@redhat.com> 2.0-2 
- Added review comments
* Fri Aug 25 2011 Anish Patil <apatil@redhat.com> 2.0-1 
- Initial packaging

