with import <nixpkgs> {};

( let
    syns = python37.pkgs.buildPythonPackage rec {
      pname = "syns";
      version = "1.0";

      src = python37.pkgs.fetchPypi {
        inherit pname version;
        sha256 = "0i72hbfvizgqyxfpkw0n92h7r0mybkma9pjx4qqja9d8rm3ikjag";
      };

      doCheck = false;

      propagatedBuildInputs = [ pkgs.python37Packages.requests ];

      meta = {
        homepage = "https://github.com/boi4/syns/";
        description = "List processing tools and functional utilities";
	license = licenses.gpl3;
      };
    };

  in python37.withPackages (ps: [syns])
).env
