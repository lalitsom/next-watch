{
  description = "next-watch flake";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-23.05-darwin";
  outputs = { self, nixpkgs }: {
    devShell.aarch64-darwin = nixpkgs.legacyPackages.aarch64-darwin.mkShell {
      buildInputs = with nixpkgs.legacyPackages.aarch64-darwin; [
        python310
        python310Packages.pip
        python310Packages.faiss
        python310Packages.numpy
        python310Packages.pandas
      ];

    shellHook = ''
        echo "Entered python shell for next-watch-nix project:"
      '';
    };
  };
}