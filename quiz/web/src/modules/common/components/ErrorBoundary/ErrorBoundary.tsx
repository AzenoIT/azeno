import { Component, ErrorInfo, ReactNode } from "react";

interface Props {
    children: ReactNode;
}

interface State {
    hasError: boolean;
}

class ErrorBoundary extends Component<Props, State> {
    public constructor(props: Props) {
        super(props);
        this.state = {
            hasError: false,
        };
    }

    public static getDerivedStateFromError(): State {
        return { hasError: true };
    }

    public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
        // eslint-disable-next-line no-console
        console.error("Uncaught error:", error, errorInfo);
    }

    public render() {
        const { hasError } = this.state;
        const { children } = this.props;
        if (hasError) {
            return (
                <div className="flex flex-col h-full justify-center text-center">
                    <h1 className="text-4xl text-white">Sorry</h1>
                    <p className="text-xl text-white mb-10">Something went wrong, please try again</p>
                </div>
            );
        }
        return children;
    }
}

export default ErrorBoundary;
