import { useEffect, useState } from "react";
import useConversation from "../zustand/useConversation";
import toast from "react-hot-toast";

const useGetMessages = () => {
	const [loading, setLoading] = useState(false);
	const { messages, setMessages, selectedConversation } = useConversation();

	useEffect(() => {
		const getMessages = async () => {
			setLoading(true);
			try {
				const d = await JSON.parse(localStorage.getItem("chat-user"));
				const res = await fetch(`/api/messages/${selectedConversation.id}`, {
					headers: { "Content-Type": "application/json", "Authorization": `Bearer ${d.token[0]}` }
				});
				const data = await res.json();
				if (data.error) throw new Error(data.error);
				setMessages(data);
			} catch (error) {
				toast.error(error.message);
			} finally {
				setLoading(false);
			}
		};

		if (selectedConversation?.id) getMessages();
	}, [selectedConversation?.id, setMessages]);

	return { messages, loading };
};
export default useGetMessages;
