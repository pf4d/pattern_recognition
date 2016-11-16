from scipy.sparse            import spdiags
from pylab                   import *
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors       import from_levels_and_colors
from matplotlib              import colors

mpl.rcParams['font.family']     = 'serif'
mpl.rcParams['legend.fontsize'] = 'medium'

def plot_matrix(M, title, name, continuous=False, cmap='Greys', scale='lin',
                numLvls=12, Mmin=None, Mmax=None, xlabel=None, ylabel=None,
                direc='./', figsize=(5,5)):
  """
  plot a matrix <M> with title <title> and a colorbar.
  """

  fig = figure(figsize=figsize)
  ax  = fig.add_subplot(111)
  
  if Mmin == None:
    Mmin = M.min()
  if Mmax == None:
    Mmax = M.max()
  
  # countour levels :
  if scale == 'log':
    M[M <= Mmin] = Mmin + 1e-16
    M[M >= Mmax] = Mmax - 1e-16
    from matplotlib.ticker import LogFormatter
    levels      = np.logspace(np.log10(Mmin), np.log10(Mmax), numLvls)
    formatter   = LogFormatter(10, labelOnlyBase=False)
    norm        = colors.LogNorm()
  
  elif scale == 'lin':
    from matplotlib.ticker import ScalarFormatter
    M[M < Mmin] = Mmin + 1e-16
    M[M > Mmax] = Mmax - 1e-16
    levels    = np.linspace(Mmin, Mmax, numLvls)
    formatter = ScalarFormatter()
    norm      = None
  
  M    = array(M)
  m,n  = shape(M)
  cmap = cm.get_cmap(cmap)

  if xlabel is not None:
    x_pos  = arange(n)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(xlabel, rotation=90)

  if ylabel is not None:
    y_pos  = arange(m)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(ylabel)
  
  if not continuous:
    unq  = unique(M)
    num  = len(unq)
  im      = ax.imshow(M, cmap=cmap, interpolation='None', norm=norm)
  tick_params(axis='both', which='both', length=0.0)
  #subplots_adjust(left=0.5, bottom=0.5)
  divider = make_axes_locatable(ax)
  cax     = divider.append_axes("right", size="5%", pad=0.05)
  dim     = r'$%i \times %i$ ' % (m,n)
  ax.set_title(dim + title)
  #ax.axis('off')
  cb = colorbar(im, cax=cax)
  if not continuous:
    cb.set_ticks(unq)
    cb.set_ticklabels(unq)

  tight_layout()
  savefig(direc + name + '.pdf')#, dpi=200)
  show()



