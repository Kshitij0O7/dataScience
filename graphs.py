from regression import y, betas, slope,intercept
import matplotlib.pyplot as plt
import numpy as np

# Plot empirical SML
plt.scatter(betas, y)
plt.xlabel('Beta')
plt.ylabel('Average Returns')
plt.title('Empirical Security Market Line (SML)')
plt.grid(True)

# Add CAPM line
CAPM_line = intercept + slope * np.array(betas)
plt.plot(betas, CAPM_line, color='red', label='CAPM Line')

plt.legend()
plt.show()