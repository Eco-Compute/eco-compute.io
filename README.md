# eco-compute.io

We are using the theme: Vixcon.

Documentation is to be found here: https://docs.gethugothemes.com/vixcon/installation/

## Buildung

Just do `hugo`

No `npm` packages or similar need to be installed

## Local editing

Just do `hugo server`

Different to normal *HUGO* sites most of the editing happens in the `*.yml` files. For instance the pricing details are editied in the https://github.com/Eco-Compute/eco-compute.io/blob/main/data/en/pricing.yml file and not in the https://github.com/Eco-Compute/eco-compute.io/blob/main/content/english/pricing/_index.md file.

Also, for stuff that is displayed on the landing page, most stuff is done via https://github.com/Eco-Compute/eco-compute.io/blob/main/data/en/homepage.yml

For all other and global config the https://github.com/Eco-Compute/eco-compute.io/blob/main/config.toml is used as usual

## Pictures from

- https://www.pexels.com/photo/photo-of-people-sitting-on-chairs-3321789/
- https://www.pexels.com/photo/women-sitting-on-chairs-inside-a-room-3719037/

## Redirects

Please note that the magic `_redirects` file must be in the file `/public` directory.

One hack to achieve this is to put it in the `/static` dir, as this will be copied over on build