#R

#' @importFrom utils packageVersion
.onAttach <- function(lib, pkg){
	if(interactive()){
		version <- packageVersion('bfabricShiny')
		packageStartupMessage("Package 'bfabricShiny' version ", version)
	  invisible()
	}
}
