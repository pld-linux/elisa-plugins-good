Summary:	"Good" plugins for elisa
Summary(pl.UTF-8):	"Dobre" wtyczki dla elisy
Name:		elisa-plugins-good
Version:	0.5.12
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	9ced304cc1a009ad123f2888ad472bd9
URL:		http://www.fluendo.com/elisa/
BuildRequires:	elisa = %{version}
Provides:	elisa-plugins = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Good" plugins for elisa

%description -l pl.UTF-8
"Dobre" wtyczki dla elisy

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/elisa/plugins/*
