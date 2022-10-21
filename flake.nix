{
  description = "Flake of game list project";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let

        pkgsAllowUnfree = import nixpkgs {
          system = "x86_64-linux";
          config = { allowUnfree = true; };
        };
      in
      {
        devShell = pkgsAllowUnfree.mkShell {
          buildInputs = with pkgsAllowUnfree; [
            python3
          ];

          shellHook = ''
            echo "Entering the nix devShell in alura-flask-game-list"
          '';
        };
      }
    );
}
