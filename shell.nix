{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pygame
    ]))
    pkgs.pyright
    pkgs.black
  ];
}
