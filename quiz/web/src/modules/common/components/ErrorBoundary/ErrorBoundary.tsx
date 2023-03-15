import { Component, ErrorInfo, ReactNode } from "react";

interface Props {
    children?: ReactNode;
}

interface State {
    hasError: boolean;
}

class ErrorBoundary extends Component<Props, State> {
    public state: State = {
        hasError: false,
    };

    public static getDerivedStateFromError(_: Error): State {
        return { hasError: true };
    }

    public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
        console.error("Uncaught error:", error, errorInfo);
    }

    public render() {
        if (this.state.hasError) {
            return (
                <div className="flex flex-col h-full justify-center text-center">
                    <h1 className={"text-4xl text-white"}>Sorry</h1>
                    <p className={"text-xl text-white mb-10"}>Something went wrong, please try again</p>
                </div>
            );
        }

        return this.props.children;
    }
}

export default ErrorBoundary;
