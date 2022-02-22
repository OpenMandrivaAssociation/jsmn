#global debug_package %{nil}

# header only package
%define devname	%mklibname %{name} -d

%bcond_without examples
%bcond_without tests

Summary:	A world fastest JSON parser/tokenizer
Name:		jsmn
Version:	1.1.0
Release:	1
License:	MIT
Group:		Development/C
URL:		https://github.com/zserge/jsmn
Source0:	https://github.com/zserge/jsmn/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

%description
jsmn (pronounced like 'jasmine') is a minimalistic JSON parser in C. It can
be easily integrated into resource-limited or embedded projects.

Most JSON parsers offer you a bunch of functions to load JSON data, parse it
and extract any value by its name. jsmn proves that checking the correctness
of every JSON packet or allocating temporary objects to store parsed JSON
fields often is an overkill.

jsmn is designed to be robust (it should work fine even with erroneous data),
fast (it should parse data on the fly), portable (no superfluous dependencies
or non-standard C extensions). And of course, simplicity is a key
feature - simple code style, simple algorithm, simple integration into other
projects.

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	A world fastest JSON parser/tokenizer header only library
Provides:	%{name}-devel

%description -n %{devname}
jsmn (pronounced like 'jasmine') is a minimalistic JSON parser in C. It can
be easily integrated into resource-limited or embedded projects.

Most JSON parsers offer you a bunch of functions to load JSON data, parse it
and extract any value by its name. jsmn proves that checking the correctness
of every JSON packet or allocating temporary objects to store parsed JSON
fields often is an overkill.

jsmn is designed to be robust (it should work fine even with erroneous data),
fast (it should parse data on the fly), portable (no superfluous dependencies
or non-standard C extensions). And of course, simplicity is a key
feature - simple code style, simple algorithm, simple integration into other
projects.

%files -n %{devname}
%license LICENSE
%doc README.md
%{_includedir}/%{name}.h

#---------------------------------------------------------------------------

%if %{with examples}
%package examples
Summary:	example for jsmn
Requires:	%{name}= %{version}-%{release}

%description examples
jsmn examples.

%files examples
%{_bindir}/*
%{_datadir}/%{name}/examples
%endif

#---------------------------------------------------------------------------

%prep
%autosetup

%build
%{set_build_flags}
#make_build

%if %{with examples}
%make_build simple_example jsondump
%endif

%install
#make_install

install -dm 0755 %{buildroot}%{_includedir}
install -pm 0644 %{name}.h %{buildroot}%{_includedir}

%if %{with examples}
install -dm 0755 %{buildroot}%{_bindir}
for e in jsondump simple_example
do
	install -pm 0755 $e %{buildroot}%{_bindir}
done

install -dm 0755 %{buildroot}%{_datadir}/%{name}/examples
install -pm 0644 example/*c %{buildroot}%{_datadir}/%{name}/examples
%endif

%if %{with tests}
%check
make test
%endif

