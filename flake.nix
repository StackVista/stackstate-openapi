{
  description = "StackState OpenApi";

  nixConfig.bash-prompt = "STS OpenApi 2 $ ";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {

        devShell = pkgs.mkShell {
          buildInputs = (with pkgs; [
            openapi-generator-cli
            nodejs-14_x
            bash
            redoc-cli
            awscli
          ]);
        };
      });
}
