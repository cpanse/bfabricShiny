% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/ms_queue.R
\name{generate_queue}
\alias{generate_queue}
\title{FGCZ mass spec queue generator}
\usage{
generate_queue(
  x,
  foldername = "",
  projectid = 1000,
  area = "Proteomics",
  instrument = "LUMOS_2",
  username = "cpanse",
  autoQC01 = "TRUE",
  QC01o = 3,
  QC01m = 1,
  autoQC02 = "FALSE",
  QC02o = 0,
  QC02m = 1,
  autoQC4L = "FALSE",
  QC4Lo = 4,
  QC4Lm = 1,
  clean = "TRUE",
  cleano = 4,
  cleanm = 1,
  start1 = 1,
  start2 = NA,
  start3 = NA,
  end1 = 1,
  end2 = NA,
  end3 = NA,
  lists = 1,
  startposition = 1,
  nr.methods = 2,
  nr.replicates = 3,
  qc.type = 1,
  method = "default",
  pathprefix = "D:\\\\Data2San",
  pathprefixsep = "\\\\",
  DEBUG = FALSE,
  order = TRUE,
  startpos = list(row = 1, col = "A", plate = 1)
)
}
\arguments{
\item{x}{x}

\item{foldername}{forder name}

\item{projectid}{foldername}

\item{area}{Proteomics or Metabolomics}

\item{instrument}{LTQFT_1}

\item{username}{cpanse}

\item{nr.methods}{1}

\item{nr.replicates}{1}

\item{qc.type}{TODO}

\item{method}{random}

\item{pathprefix}{D:Data2San}

\item{pathprefixsep}{'/'}

\item{how.often}{1}

\item{how.many}{1}

\item{showcondition}{TODO}

\item{hplc}{TODO}
}
\value{
a instrument configuration as \code{data.frame}.
}
\description{
FGCZ mass spec queue generator
}
\examples{
generate_queue(x <- bfabricShiny:::.test_data_medium(),start2 = NA,start3 = NA)
generate_queue(x <- bfabricShiny:::.test_data_medium(),
   projectid = 3000,
   area = "Proteomics",
   instrument = "QEXACTIVE_2",
   username = "roschi",
   autoQC01 = "TRUE",
   QC01o = 4,
   QC01m = 1,
   autoQC02 = "FALSE",
   QC02o = 4,
   QC02m = 1,
   autoQC4L = "FALSE",
   QC4Lo = 4,
   QC4Lm = 1,
   clean = "FALSE",
   cleano = 4,
   cleanm = 1,
   start1 = 1,
   start2 = NA,
   start3 = NA,
   end1 = 4,
   end2 = 1,
   end3 = 3,
   lists = 1,
   startposition = 1,
   nr.methods = 1,
   nr.replicates = 1,
   qc.type = 1,
   method = "default",
   pathprefix = "D:Data2San")
generate_queue(bfabricShiny:::.test_data_single() , order=TRUE, startpos = list(row=3, col="A", plate=2))
generate_queue(bfabricShiny:::.test_data_medium() , order=FALSE)
generate_queue(bfabricShiny:::.test_data_single())
generate_queue(bfabricShiny:::.test_data_large())
generate_queue(bfabricShiny:::.test_data_medium_random())

generate_queue(bfabricShiny:::.test_data_medium_random(), method = "default")
generate_queue(bfabricShiny:::.test_data_medium_random(), method = "random")
\dontrun{

generate_queue(bfabricShiny:::.test_data_medium(), method = "blockrandom")
}
bfabricShiny:::.test_data_medium()
generate_queue(bfabricShiny:::.test_data_medium())

}
