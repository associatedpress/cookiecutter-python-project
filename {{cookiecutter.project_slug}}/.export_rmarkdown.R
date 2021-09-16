main <- function() {
  # Exports Rmd as html from the command line.
  #
  # Takes one argument:
  # Rmd file to convert
  #
  library(rmarkdown)
  args <- commandArgs(trailingOnly = TRUE)
  rmarkdown_file <- args[1]
  render(rmarkdown_file, output_dir='data/html_reports')
}

main()