return { 
  "catppuccin/nvim", 
  name = "catppuccin", 
  priority = 999,
  config = function()
    require('catppuccin').setup({
        transparent_background = true,
        term_colors = false,
    })  
    vim.cmd.colorscheme "catppuccin"
  end
}



