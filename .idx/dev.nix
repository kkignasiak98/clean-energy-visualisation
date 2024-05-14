# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python310
    pkgs.python310Packages.pip
  ];

  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
       "vscodevim.vim"
       "ms-toolsai.jupyter"
       "codeium.codeium"
       "ms-python.python"
       "aaron-bond.better-comments"
       "eamodio.gitlens"
       "charliermarsh.ruff"
       
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      # It might not work if you want to rebuild it along the way.
      onCreate = {
         virtual_env = "python3 -m venv main-venv";
      };
      onStart = {
          virtual_env = "python3 -m venv main-venv";
          install_pip_tools = "pip install pip-tools==7.4.1";
          install_python_packages = "source main-venv/bin/activate && pip install -r requirements/prod.txt";
          
      };
    };
  };
}
