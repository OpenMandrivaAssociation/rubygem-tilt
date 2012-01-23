# Generated from tilt-1.3.3.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	tilt

Summary:	Generic interface to multiple Ruby template engines
Name:		rubygem-%{rbname}

Version:	1.3.3
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/rtomayko/tilt/
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Generic interface to multiple Ruby template engines

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/tilt
%{ruby_gemdir}/gems/%{rbname}-%{version}/
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec


%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
