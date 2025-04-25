// src/theme.ts
export const theme = {
    colors: {
      primary: '#3b82f6',
      secondary: '#6366f1',
      background: '#f8fafc',
      card: '#ffffff',
      text: '#1e293b',
      subtext: '#64748b',
      muted: '#94a3b8',
      border: '#e2e8f0',
      gradient: 'linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%)',
      buttonGradient: 'linear-gradient(45deg, #3b82f6 0%, #6366f1 100%)',
    },
    typography: {
      title: {
        fontSize: '28px',
        fontWeight: 700,
        fontFamily: "'Inter', sans-serif",
        letterSpacing: '-0.02em',
      },
      paragraph: {
        fontSize: '16px',
        lineHeight: 1.6,
      },
      small: {
        fontSize: '14px',
      },
    },
    spacing: {
      small: '8px',
      medium: '16px',
      large: '24px',
      xlarge: '32px',
      xxlarge: '48px',
    },
    shadows: {
      card: '0 12px 24px rgba(0, 0, 0, 0.05)',
      button: '0 4px 12px rgba(59,130,246,0.25)',
    },
    borderRadius: {
      small: '8px',
      medium: '12px',
      large: '16px',
    },
  };